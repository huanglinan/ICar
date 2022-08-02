import { Component, OnInit } from '@angular/core';
import { Brand } from 'src/app/entities/Brand';
import { BrandsService } from 'src/app/services/brands.service';
import { NzMessageService } from 'ng-zorro-antd/message';
import { NzUploadFile } from 'ng-zorro-antd/upload';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { DomSanitizer } from '@angular/platform-browser';
import { Router } from '@angular/router';

export const getBase64 = (file: File): Promise<string | ArrayBuffer | null> =>
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
  previewImage: string | undefined = '';
  previewVisible = false;
  fileList: NzUploadFile[] = [];
  validateForm!: FormGroup;
  brands: Brand[] = [];
  isVisibleModal = false
  selectedBrand: Brand
  isOkLoading = false;
  searchText: string = "";

  constructor(private brandsService: BrandsService, private msg: NzMessageService, private fb: FormBuilder, private domSanitizer: DomSanitizer, private router: Router) { }

  ngOnInit(): void {
    this.brandsService.getLists().subscribe(res => {
      this.brands = res.data
      this.brands.forEach(element => {
        this.brandsService.getLogo(element.logo).subscribe(res => {
          element.logo = this.domSanitizer.bypassSecurityTrustUrl(URL.createObjectURL(res))
        })
      });
    })
  }

  public searchData(): void {
    this.brandsService.searchBrands(this.searchText).subscribe(res => {
      this.brands = res.data
      this.brands.forEach(element => {
        this.brandsService.getLogo(element.logo).subscribe(res => {
          element.logo = this.domSanitizer.bypassSecurityTrustUrl(URL.createObjectURL(res))
        })
      });
    })
  }

  handlePreview = async (file: NzUploadFile): Promise<void> => {
    if (!file.url && !file.preview) {
      file.preview = await getBase64(file.originFileObj!);
    }
    this.previewImage = file.url || file.preview;
    this.previewVisible = true;
  };


  showModal(): void {
    this.isVisibleModal = true;
  }
  showExceptionError = false

  handleOk(): void {
    this.isOkLoading = true;
    this.showExceptionError = false;
    if (this.validateForm.valid) {
      let brand = new Brand()
      brand.name = this.validateForm.value.name;
      brand.desc = this.validateForm.value.desc;
      brand.is_active = this.validateForm.value.is_active;
      if (this.fileList.length > 0)
        brand.logo = this.fileList[0].response.data;
      this.brandsService.createBrand(brand).subscribe(
        res => {
          debugger
          this.isVisibleModal = false;
          this.isOkLoading = false;
        },
        error => {
          debugger
          this.isOkLoading = false;
          this.showExceptionError = true;
        }
      )
    } else {
      Object.values(this.validateForm.controls).forEach(control => {
        if (control.invalid) {
          control.markAsDirty();
          control.updateValueAndValidity({ onlySelf: true });
        }
      });
    }

  }


  public handleCancel(): void {
    this.selectedBrand = null;
    this.isVisibleModal = false;
    this.isOkLoading = false;
  }

  public openModal() {
    this.validateForm = this.validateForm = this.fb.group({
      name: [null, [Validators.required]],
      desc: [null, [Validators.required]],
      is_active: [true]
    });
    this.fileList = []
    this.selectedBrand = new Brand()
    this.isVisibleModal = true
  }

  // public openModal(id: string) {
  //   if (id !== '') {
  //     this.brandsService.getBrandById(id).subscribe(res => {
  //       this.selectedBrand = res.data
  //       console.log(this.selectedBrand.logo)
  //       this.brandsService.getLogo(this.selectedBrand.logo).subscribe(res => {
  //         this.selectedBrand.logo = this.domSanitizer.bypassSecurityTrustUrl(URL.createObjectURL(res))
  //       })
  //     })
  //     this.isVisible = true
  //   }
  // }
  public viewDetail(id: string) {
    // Pass along the hero id if available
    // so that the HeroList component can select that item.
    this.router.navigate(['/detail', { id: id }]);
  }
}
