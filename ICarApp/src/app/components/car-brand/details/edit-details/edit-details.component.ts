import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { DomSanitizer } from '@angular/platform-browser';
import { ActivatedRoute, Router } from '@angular/router';
import { NzUploadFile } from 'ng-zorro-antd/upload';
import { Brand } from 'src/app/entities/Brand';
import { BrandsService } from 'src/app/services/brands.service';
import { getBase64 } from '../../car-brand.component';


@Component({
  selector: 'app-edit-details',
  templateUrl: './edit-details.component.html',
  styleUrls: ['./edit-details.component.scss']
})
export class EditDetailsComponent implements OnInit {
  previewImage: string | undefined = '';
  previewVisible = false;
  fileList: NzUploadFile[] = [];
  validateForm!: FormGroup;
  isVisibleModal = false
  brand: Brand;
  selectedId: string

  constructor(private brandsService: BrandsService, private route: ActivatedRoute, private domSanitizer: DomSanitizer,private fb: FormBuilder, private router: Router) { }

  ngOnInit(): void {
    this.selectedId = this.route.snapshot.paramMap.get('id');
    this.brandsService.getBrandById(this.selectedId).subscribe(res => { 
      this.brand = res.data
      this.brandsService.getLogo(this.brand.logo).subscribe(ress => {
        this.brand.logo = this.domSanitizer.bypassSecurityTrustUrl(URL.createObjectURL(ress))
      })
     
     });
    this.validateForm = this.validateForm = this.fb.group({
      name: [null, [Validators.required]],
      desc: [null, [Validators.required]],
      is_active: [true]
    });
    
  }
  handlePreview = async (file: NzUploadFile): Promise<void> => {
    if (!file.url && !file.preview) {
      file.preview = await getBase64(file.originFileObj!);
    }
    this.previewImage = file.url || file.preview;
    this.previewVisible = true;
  };

  public submitForm() {
    console.log(this.validateForm.valid)
    if (this.validateForm.valid) {
      debugger
      let brandUp = new Brand()
      brandUp.id = this.brand.id
      brandUp.name = this.validateForm.value.name;
      brandUp.desc = this.validateForm.value.desc;
      brandUp.is_active = this.validateForm.value.is_active;
      if(this.fileList.length > 0)
        brandUp.logo = this.fileList[0].response.data;
      this.brandsService.putBrand(brandUp).subscribe(
        res => {
          debugger
        },
        error => {
          debugger
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
}
