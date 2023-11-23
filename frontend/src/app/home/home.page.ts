import { Component, AfterViewInit, ChangeDetectorRef, ViewChild } from '@angular/core';
import Chart from 'chart.js/auto';
import { webSocket } from 'rxjs/webSocket';
import annotationPlugin from 'chartjs-plugin-annotation';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage implements AfterViewInit {
  
  public socket;
  public chart: any;
  public chartPeso:any;

  public values: any[] = [0];
  public umidade = 0
  public temperatura = 0
  public vazamento = false
  public quantidadePeso = 0


  alertOpen:boolean = false



  constructor(
    private cdr: ChangeDetectorRef,
  ) {
    this.socket = webSocket('ws://172.20.10.2:8000/ws/iot');
  }

  ngAfterViewInit() {
    this.startConnWs();
    const ctx = document.getElementById('chartCanvas') as HTMLCanvasElement;
    const ctx2 = document.getElementById('chartCanvas2') as HTMLCanvasElement;
    Chart.register(annotationPlugin);

    this.chart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['Gás (ppm)'],
        datasets: [{
          label: 'Gás (ppm',
          data: this.values,
          backgroundColor: '#00FFA3',
          borderColor: '#3D70FF',
          borderWidth: 2,
        }]
      },
      options: {
        indexAxis: 'y', 
        scales: {
          y: {
            beginAtZero: true,
            min: 0,
            max: 1200,
          },
          x: {
            beginAtZero: true,
            min: 0,
            max: 1200,
          }
        },
        plugins: {
          annotation: {
            annotations: {
              line1: {
                type: 'line',
                xMin: 1000,
                xMax: 1000,
                borderColor: 'rgb(255, 99, 132)',
                borderWidth: 2,
          
                
              }
            }
          }
        } 
      }
    });
  
    this.chartPeso = new Chart(ctx2, {
      type: 'bar',
      data: {
        labels: ['Quantidade(Kg)'],
        datasets: [{
          label: '(Kg)',
          data: this.quantidadePeso, 
          backgroundColor: '#FF5733',
          borderColor: '#FF5733',
          borderWidth: 2,
        }]
      },
      options: {
        indexAxis: 'y', 
      
      }
    });
  }
  


  startConnWs() {
    this.socket.subscribe(
      (message: any) => {
        console.log('Mensagem recebida do servidor WebSocket:', message);

        let sensorGas = message.data.sensorGas;
        let umidadeReceived = message.data.umidade;
        let temperaturaReceived = message.data.temperatura;
        let quantidadeReceived = message.data.quantidade_peso
        let vazamentoReceived =  message.data.vazamento;

        console.log(sensorGas);
        console.log(this.values);
        if (sensorGas !== undefined) {
          this.values[0] = sensorGas  
          this.chart.update();
        }

        if(umidadeReceived !== undefined){
          this.umidade = umidadeReceived
          this.cdr.detectChanges();
        }

        if(temperaturaReceived !== undefined){
          this.temperatura = temperaturaReceived
          this.cdr.detectChanges();
        }

        if(quantidadeReceived !== undefined){
          this.quantidadePeso = quantidadeReceived
          this.cdr.detectChanges();
        }


        if(vazamentoReceived == true){
          this.alertOpen = true
        }
        
        
      },
      (error:any) => {
        console.error('Erro na conexão com o servidor WebSocket:', error);
      }
    );
  }


  ignoreAlert(){
    this.alertOpen = false
  }


  async callFireMan() {
    try {
      window.location.href = 'tel:193';
    } catch (error) {
      console.error('Erro ao tentar fazer a chamada:', error);
    }
  }
  
  
  

}
