import { Component, OnInit, Inject } from '@angular/core';
import {MatDialog} from '@angular/material';
import {Router} from '@angular/router';
import { DialogComponent } from '../dialog/dialog.component';
import {MatSnackBar} from '@angular/material';
@Component({
  selector: 'app-welcome',
  templateUrl: './welcome.component.html',
  styleUrls: ['./welcome.component.css']
})
export class WelcomeComponent implements OnInit {
  modal;
  dialogRef;
  email: string;
  password: string;
  constructor(
    private router: Router,
    public dialog: MatDialog,
    public snackBar: MatSnackBar,
  ) { }

  ngOnInit() {
  }
  loginModal(): void {
    this.dialogRef = this.dialog.open(DialogComponent, {
      width: '250px',
      data: { email: this.email, password: this.password}
    });
    this.dialogRef.afterClosed().subscribe(result => {
      if (result.email != null) {
        this.email = result.email;
        this.password = result.password;
        this.checkCred();
      }
    });
  }
  checkCred() {
    if (this.email === 'yuli@gmail.com' && this.password === 'yuli=best') {
      this.router.navigate(['/home']);
      this.snackBar.open('Welcome!', 'X', {duration: 2000, extraClasses: ['loginSuccess-snackbar']});
    } else {
      this.snackBar.open('Oops, incorrect email/username or passowrd.', 'Got It', {duration: 3000, extraClasses: ['loginFail-snackbar']});
    }
  }

}
