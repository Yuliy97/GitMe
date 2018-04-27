import { Component, OnInit, Inject } from '@angular/core';
import {MatDialog} from '@angular/material';
import {Router} from '@angular/router';
import { DialogComponent } from '../dialog/dialog.component';
import {MatSnackBar} from '@angular/material';
import { AuthService } from '../auth.service';
import { NgxSpinnerService } from 'ngx-spinner';
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
  isLoading: boolean;
  constructor(
    private spinner: NgxSpinnerService,
    private router: Router,
    public dialog: MatDialog,
    public snackBar: MatSnackBar,
    private _authService: AuthService,
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
    this.spinner.show()
    this._authService.authenticate_user(this.email, this.password).subscribe(
      data => {
        if ( data === 'Authorized') {
          this._authService.update_database(this.email, this.password).subscribe(
            data => {

              this.spinner.hide()

              this.router.navigate(['/home']);
          this.snackBar.open('Welcome!', 'X', {duration: 2000, extraClasses: ['loginSuccess-snackbar']});
            }
          );
        } else {
          this.spinner.hide()
          this.snackBar.open(data, 'Got It', {duration: 3000, extraClasses: ['loginFail-snackbar']});
        }
      }
    );
  }
  getUsername() {
    return this.email;
  }


}
