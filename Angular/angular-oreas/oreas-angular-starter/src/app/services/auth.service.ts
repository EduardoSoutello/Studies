import { Injectable, signal } from '@angular/core';

@Injectable({ providedIn: 'root' })
export class AuthService {
  user = signal<{ email: string } | null>(null);

  login(email: string) {
    this.user.set({ email });
  }
  logout() {
    this.user.set(null);
  }
}
