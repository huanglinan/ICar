import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CarBrandComponent } from './components/car-brand/car-brand.component';
import { EditDetailsComponent } from './components/car-brand/details/edit-details/edit-details.component';
import { ViewDetailsComponent } from './components/car-brand/details/view-details/view-details.component';

const routes: Routes = [
  { path: '', pathMatch: 'full', redirectTo: 'car_brand' },
  { path: 'car_brand', component: CarBrandComponent },
  { path: 'detail', component: ViewDetailsComponent },
  { path: 'edit', component: EditDetailsComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
