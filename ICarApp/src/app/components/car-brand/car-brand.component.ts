import { Component, OnInit } from '@angular/core';
import { Brand } from 'src/app/entities/Brand';
import { BrandsService } from 'src/app/services/brands.service';
import { NzMessageService } from 'ng-zorro-antd/message';
import { NzUploadFile } from 'ng-zorro-antd/upload';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { DomSanitizer } from '@angular/platform-browser';

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
  // brands: any;
  previewImage: string | undefined = '';
  previewVisible = false;
  fileList: NzUploadFile[] = [];
  validateForm!: FormGroup;
  brands: Brand[]=[];

  constructor(private brandsService: BrandsService, private msg: NzMessageService, private fb: FormBuilder, private domSanitizer: DomSanitizer) { }

  ngOnInit(): void {
    this.brandsService.getLists().subscribe(res => {
      this.brands = res.data
      this.brands.forEach(element => {
        this.brandsService.getLogo(element.logo).subscribe( res => {
          element.logo =  this.domSanitizer.bypassSecurityTrustUrl(URL.createObjectURL(res))
        })
      });
    })

    this.validateForm = this.fb.group({
      name: [null, [Validators.required]],
      desc: [null, [Validators.required]]
    });
  }

  public submitForm() {
    debugger
    console.log('file', this.fileList);
    console.log('file', this.fileList[0].response.data);
    if (this.validateForm.valid) {
      console.log('submit OK', this.validateForm.value);
      let brand = new Brand()
      brand.name = this.validateForm.value.name;
      brand.desc = this.validateForm.value.desc;
      brand.logo = this.fileList[0].response.data;
      this.brandsService.createBrand(brand).subscribe()
    } else {
      Object.values(this.validateForm.controls).forEach(control => {
        if (control.invalid) {
          control.markAsDirty();
          control.updateValueAndValidity({ onlySelf: true });
        }
      });
    }
  }


  public onClick() {

  }

  handlePreview = async (file: NzUploadFile): Promise<void> => {
    if (!file.url && !file.preview) {
      file.preview = await getBase64(file.originFileObj!);
    }
    this.previewImage = file.url || file.preview;
    this.previewVisible = true;
  };
}
