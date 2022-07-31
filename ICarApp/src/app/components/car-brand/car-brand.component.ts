import { Component, OnInit } from '@angular/core';
import { Brand } from 'src/app/entities/Brand';
import { BrandsService } from 'src/app/services/brands.service';
import { NzMessageService } from 'ng-zorro-antd/message';
import { NzUploadFile } from 'ng-zorro-antd/upload';

const getBase64 = (file: File): Promise<string | ArrayBuffer | null> =>
  new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = () => resolve(reader.result);
    reader.onerror = error => reject(error);
  });

@Component({
  selector: 'app-car-brand',
  templateUrl: './car-brand.component.html',
  styleUrls: ['./car-brand.component.scss']
})
export class CarBrandComponent implements OnInit {
  brands: any;
  newBrand: Brand;
  previewImage: string | undefined = '';
  previewVisible = false;
  fileList: NzUploadFile[] = []


  handlePreview = async (file: NzUploadFile): Promise<void> => {
    if (!file.url && !file.preview) {
      file.preview = await getBase64(file.originFileObj!);
    }
    this.previewImage = file.url || file.preview;
    this.previewVisible = true;
  };
  constructor(private brandsService: BrandsService, private msg: NzMessageService) { }

  ngOnInit(): void {
    this.newBrand = new Brand()
    this.brandsService.getLists().subscribe(res => {
      this.brands = res.data
      console.log(this.brands)
    })
  }

  public submitForm() {

  }
  public onClick() {

  }

}
