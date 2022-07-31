import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class BrandsService {

  constructor(private httpClient: HttpClient) { }
  getLists(): Observable<any>{
    return this.httpClient.get<any>('http://127.0.0.1:8000/api/v1/brands')
  }


}
