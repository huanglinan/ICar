import { Component, OnInit } from '@angular/core';
import { DomSanitizer } from '@angular/platform-browser';
import { ActivatedRoute, Router } from '@angular/router';
import { Brand } from 'src/app/entities/Brand';
import { BrandsService } from 'src/app/services/brands.service';
@Component({
  selector: 'app-view-details',
  templateUrl: './view-details.component.html',
  styleUrls: ['./view-details.component.scss']
})
export class ViewDetailsComponent implements OnInit {

  constructor(private brandsService: BrandsService, private route: ActivatedRoute, private domSanitizer: DomSanitizer, private router: Router) { }
  brand: Brand;
  selectedId: string
  ngOnInit(): void {
    this.selectedId = this.route.snapshot.paramMap.get('id');
    this.brandsService.getBrandById(this.selectedId).subscribe(res => { 
      this.brand = res.data
      this.brandsService.getLogo(this.brand.logo).subscribe(ress => {
        this.brand.logo = this.domSanitizer.bypassSecurityTrustUrl(URL.createObjectURL(ress))
      })
     });
      
  }
  public edit(id: string){
    this.router.navigate(['/edit', { id: id }]);
  }

}
