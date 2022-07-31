import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CarBrandComponent } from './components/car-brand/car-brand.component';

const routes: Routes = [
  { path: '', pathMatch: 'full', redirectTo: 'car_brand' },
  { path: 'car_brand', component: CarBrandComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
}) 
export class AppRoutingModule { }
