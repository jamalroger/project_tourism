import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ajax } from 'rxjs/ajax';


@Component({
  selector: 'app-add',
  templateUrl: './add.component.html',
  styleUrls: ['./add.component.css']
})
export class AddComponent implements OnInit {
  token: any;
  data: any;
  place:any;
  img:any;
  p: number = 1;

  constructor(private http: HttpClient) {  }

  ngOnInit() {
    // first method
    // this.http.get('http://localhost:4000/sitePlace/')
    //    .subscribe((data: any)  => this.httpdata = data );
    ajax('/getSite/')
    .subscribe((res) => {

     this.data = res.response;

    });
    ajax('http://localhost:8000/getToken/')
    .subscribe((res) => {

     this.token = res.response;

    });

  }

  addToSlide(place: string,query:any){
    this.place=place;
    this.img=query;
  }

  addImg() {

      var add_img  = document.createElement("div");
      add_img.innerHTML= '<hr/> <label>Image :</label> <input name="myfiles" type="file">  <br/> <label>Description de image </label>  <br/> <textarea name="desImg" placeholder="text" style="height: 37px; width: 390px"> </textarea> ';
      document.getElementById("fileimg").appendChild(add_img);
  }





//   onFileChanged(event) {
//     this.selectedFile = event.target.files[0];
//   }

//  onUpload() {
//   // this.http is the injected HttpClient
//   const uploadData = new FormData();
//   uploadData.append('myfile', this.selectedFile, this.selectedFile.name);
//   this.http.post('http://localhost:8000', uploadData)
//     .subscribe();
//   }
}
