import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';

@Component({
  standalone: true,
  selector: 'app-login',
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {
  form = this.fb.group({
    email: ['', [Validators.required, Validators.email]],
    password: ['', [Validators.required, Validators.minLength(6)]],
    remember: [true]
  });

  loading = false;
  error = '';

  constructor(private fb: FormBuilder) {}

  submit() {
    if (this.form.invalid) {
      this.error = 'Por favor, preencha os campos corretamente.';
      return;
    }
    this.error = '';
    this.loading = true;
    setTimeout(() => {
      this.loading = false;
      alert('Login simulado com sucesso!');
    }, 800);
  }
}
