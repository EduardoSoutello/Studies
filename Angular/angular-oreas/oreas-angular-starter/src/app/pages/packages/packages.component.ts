import { Component, signal } from '@angular/core';
import { CommonModule, CurrencyPipe } from '@angular/common';
import { PackageService } from '../../services/package.service';
import { TravelPackage } from '../../models/package.model';

@Component({
  standalone: true,
  selector: 'app-packages',
  imports: [CommonModule, CurrencyPipe],
  templateUrl: './packages.component.html',
  styleUrl: './packages.component.css',
  providers: [PackageService]
})
export class PackagesComponent {
  list = signal<TravelPackage[]>([]);

  constructor(private svc: PackageService) {
    this.list.set(this.svc.getAll());
  }

  buy(p: TravelPackage) {
    alert(`Compra simulada do pacote: ${p.title}`);
  }
}
