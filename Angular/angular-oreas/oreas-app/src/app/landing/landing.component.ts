import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

interface TravelPost {
  id: number;
  title: string;
  price: string;
  excerpt: string;
  image?: string;
}

@Component({
  selector: 'app-landing',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './landing.component.html',
  styleUrls: ['./landing.component.css'],
})
export class LandingComponent {
  posts: TravelPost[] = [
    {
      id: 1,
      title: 'Pacote Europa — 10 dias',
      price: '€1.499',
      excerpt: 'Paris, Roma e Barcelona: roteiro clássico com voos e hotéis inclusos.',
      image: '/assets/europe.jpg',
    },
    {
      id: 2,
      title: 'Praias do Nordeste — 7 dias',
      price: 'R$2.199',
      excerpt: 'Hospedagem em resort, passeios e transfer. Ideal para família.',
      image: '/assets/beach.jpg',
    },
    {
      id: 3,
      title: 'Aventura Patagônia — 8 dias',
      price: 'US$2.799',
      excerpt: 'Trekking, geleiras e paisagens únicas. Pacote para aventureiros.',
      image: '/assets/patagonia.jpg',
    },
  ];
}

