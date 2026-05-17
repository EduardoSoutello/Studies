import { Injectable } from '@angular/core';
import { TravelPackage } from '../models/package.model';

@Injectable({ providedIn: 'root' })
export class PackageService {
  private data: TravelPackage[] = [
    {
      id: 'rio',
      title: 'Rio de Janeiro Essencial',
      description: '4 noites em Copacabana com city tour pelo Cristo e Pão de Açúcar.',
      price: 2899.90,
      includes: ['Aéreo ida e volta', 'Hotel 4* com café', 'Traslados'],
      featured: true
    },
    {
      id: 'salvador',
      title: 'Salvador Cultural',
      description: 'Experiência afro-brasileira com passeio pelo Pelourinho e praias.',
      price: 2499.00,
      includes: ['Aéreo', 'Hotel 3* com café', 'Passeio histórico'],
      featured: true
    },
    {
      id: 'gramado',
      title: 'Gramado Romântico',
      description: 'Final de semana das Hortênsias com fondue e passeio de vinhos.',
      price: 1999.50,
      includes: ['Ônibus executivo', 'Pousada charmosa', 'City tour vinhedos'],
      featured: true
    },
    {
      id: 'buenos-aires',
      title: 'Buenos Aires Tango',
      description: '3 noites com show de tango e city tour pelos bairros clássicos.',
      price: 3199.00,
      includes: ['Aéreo', 'Hotel 4*', 'Show de tango'],
      featured: false
    }
  ];

  getAll(): TravelPackage[] {
    return [...this.data];
  }

  getFeatured(max: number): TravelPackage[] {
    return this.data.filter(d => d.featured).slice(0, max);
  }
}
