import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { LoginComponent } from './pages/login/login.component';
import { PackagesComponent } from './pages/packages/packages.component';

export const routes: Routes = [
  { path: '', component: HomeComponent, title: 'Oreas • Início' },
  { path: 'login', component: LoginComponent, title: 'Oreas • Login' },
  { path: 'pacotes', component: PackagesComponent, title: 'Oreas • Pacotes' },
  { path: '**', redirectTo: '' }
];
