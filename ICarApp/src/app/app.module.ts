import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { NZ_I18N } from 'ng-zorro-antd/i18n';
import { en_US } from 'ng-zorro-antd/i18n';
import { registerLocaleData } from '@angular/common';
import en from '@angular/common/locales/en';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { IconsProviderModule } from './icons-provider.module';
import { NzLayoutModule } from 'ng-zorro-antd/layout';
import { NzMenuModule } from 'ng-zorro-antd/menu';
import { CarBrandComponent } from './components/car-brand/car-brand.component';
import { NzBreadCrumbModule } from 'ng-zorro-antd/breadcrumb';
import { AppComponent } from './app.component';
import { NzPageHeaderModule } from 'ng-zorro-antd/page-header';
import { NzInputModule } from 'ng-zorro-antd/input';
import { NzFormModule } from 'ng-zorro-antd/form';
import { NzButtonModule } from 'ng-zorro-antd/button';
import { NzIconModule } from 'ng-zorro-antd/icon';
import { NzCascaderModule } from 'ng-zorro-antd/cascader';
import { NzSelectModule } from 'ng-zorro-antd/select';
import { NzUploadModule } from 'ng-zorro-antd/upload';
import { NzMessageModule } from 'ng-zorro-antd/message';
import { NzModalModule } from 'ng-zorro-antd/modal';
import { NzTableModule } from 'ng-zorro-antd/table';
import { NzTagModule } from 'ng-zorro-antd/tag';
import { ViewDetailsComponent } from './components/car-brand/details/view-details/view-details.component';
import { EditDetailsComponent } from './components/car-brand/details/edit-details/edit-details.component';
registerLocaleData(en);

@NgModule({
  declarations: [
    AppComponent,
    CarBrandComponent,
    ViewDetailsComponent,
    EditDetailsComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    BrowserAnimationsModule,
    IconsProviderModule,
    NzTagModule,
    NzLayoutModule,
    NzMenuModule,
    NzBreadCrumbModule,
    NzPageHeaderModule,
    NzInputModule,
    NzFormModule,
    NzButtonModule,
    NzIconModule,
    NzCascaderModule,
    NzSelectModule,
    NzUploadModule,
    ReactiveFormsModule,
    NzMessageModule,
    NzModalModule,
    NzTableModule,

  ],
  providers: [{ provide: NZ_I18N, useValue: en_US }],
  bootstrap: [AppComponent]
})
export class AppModule { }
