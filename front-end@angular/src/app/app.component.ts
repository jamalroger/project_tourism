import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
   title: any;
   httpdata: any;
   constructor() {
    this.title = 'jamal roger';
    }

     // tslint:disable-next-line:use-life-cycle-interface
     ngOnInit() {
         }


}
