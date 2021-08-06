import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UploadService {
  url = 'http://localhost:5000/upload'
  constructor(private http: HttpClient) { }
  
  uploadImage(file): Observable<any> {
    // const formData = new FormData();
    // formData.append('file', file);
    // console.log(formData)
    return this.http.post(this.url, file)
  }
}
