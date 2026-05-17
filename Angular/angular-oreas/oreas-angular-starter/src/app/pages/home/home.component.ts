import { Component, signal } from '@angular/core';
import { RouterLink } from '@angular/router';
import { CommonModule, CurrencyPipe } from '@angular/common';
import { PackageService } from '../../services/package.service';
import { TravelPackage } from '../../models/package.model';

@Component({
  standalone: true,
  selector: 'app-home',
  imports: [CommonModule, RouterLink, CurrencyPipe],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css',
  providers: [PackageService]
})
export class HomeComponent {
  featured = signal<TravelPackage[]>([]);

  constructor(private svc: PackageService) {
    this.featured.set(this.svc.getFeatured(3));
  }
}
