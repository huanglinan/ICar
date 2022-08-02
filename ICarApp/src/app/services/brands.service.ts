import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Brand } from '../entities/Brand';

@Injectable({
  providedIn: 'root'
})
export class BrandsService {
  putBrand(brand: Brand): Observable<any> {
    return this.httpClient.put<any>(
      'http://127.0.0.1:8000/api/v1/brands/' + brand.id,
      brand
    )
  }

  getBrandById(id: string): Observable<any> {
    return this.httpClient.get<any>('http://127.0.0.1:8000/api/v1/brands/' + id)
  }

  constructor(private httpClient: HttpClient) { }

  getLists(): Observable<any> {
    return this.httpClient.get<any>('http://127.0.0.1:8000/api/v1/brands')
  }

  searchBrands(name: string): Observable<any> {
    return this.httpClient.get<any>('http://127.0.0.1:8000/api/v1/brands/search?name=' +name)
  }

  createBrand(brand: Brand): Observable<any> {
    return this.httpClient.post(
      'http://127.0.0.1:8000/api/v1/brands',
      brand
    )
  }
  getLogo(id: string): Observable<any> {
    return this.httpClient.get('http://127.0.0.1:8000/api/v1/brands/getFile/' + id, { responseType: "blob" })
  }

}
