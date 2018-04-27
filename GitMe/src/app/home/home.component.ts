import { Component, OnInit} from '@angular/core';
// import { CalendarComponent } from 'ng-fullcalendar';
// import { Options } from 'fullcalendar';
import { ProfileService } from '../profile.service';
import { FeedsService } from '../feeds.service';
import { FeedResponse } from '../feeds.service';
import { AuthService } from '../auth.service';
import { AddAccountComponent } from '../add-account/add-account.component';
import {MatDialog} from '@angular/material';
import {Router} from '@angular/router';
import {MatSnackBar} from '@angular/material';
import { ReposComponent } from '../repos/repos.component';
import { NgxSpinnerService } from 'ngx-spinner';
interface ProfileResponse {
  username: string;
  total_commits: number;
  avatar: string;
  html_url: string;
}
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
})

export class HomeComponent implements OnInit {
  addAccountRef;
  issues: FeedResponse[] = [];
  search: string;
  username: string;
  oldusername: string;
  password: string;
  totalCommit: number;
  avatar: string;
  html_url: string;
  constructor(
    private spinner: NgxSpinnerService,
    private _reposComp: ReposComponent,
    public snackBar: MatSnackBar,
    private _profileService: ProfileService,
    private _feedService: FeedsService,
    private _authService: AuthService,
    public dialog: MatDialog,
    private router: Router,
  ) {
  }
  ngOnInit() {
    this.getProfile();
    this.getFeeds();

  }
  searchFor() {

  }
  getProfile() {
    this.username =  this._authService.getUsername();
    this._profileService.getProfile(this.username).subscribe(
      data => {
        this.totalCommit = data.total_commits;
        this.html_url = data.html_url;
        this.avatar = data.avatar;
        this.username = data.username;
      }
    );
  }
  updateProfile() {
    this.username =  this._authService.getUsername();
    this._profileService.getProfile(this.username).subscribe(
      data => {
        this.totalCommit = this.totalCommit + data.total_commits;
        this.html_url = this.html_url + " , " + data.html_url;
        this.avatar = data.avatar;
        this.username = this.oldusername + " , " + data.username;
      }
    );
  }
  getFeeds() {
    this.username =  this._authService.getUsername();
    this._feedService.getFeeds(this.username).subscribe(
      data => {
        this.issues = data;
      }
    );
  }
  getMoreFeed() {
    this._feedService.getFeeds(this.username).subscribe(
      data => {
        this.issues.push(...data);
      }
    );
  }
  addAccount(): void {
    this.addAccountRef = this.dialog.open(AddAccountComponent, {
      width: '250px',
      data: { username: this.username, password: this.password}
    });
    this.addAccountRef.afterClosed().subscribe(result => {
      if (result.email != null) {
        this.oldusername = this.username;
        this.username = result.email;
        this.password = result.password;
        this.checkCred();
      }
    });
  }
  checkCred() {
    this.spinner.show();
    this._authService.authenticate_user(this.username, this.password).subscribe(
      data => {
        if ( data === 'Authorized') {
          this._authService.update_database(this.username, this.password).subscribe(
            data => {
              this._reposComp.getMoreRepo(this.username);
              this.getMoreFeed();
              this.updateProfile();
              this.spinner.hide();
            }
          );
        } else {
          this.spinner.hide();
          this.username = this.oldusername;
          this.snackBar.open(data, 'Got It', {duration: 3000, extraClasses: ['loginFail-snackbar']});
        }
      }
    );
  }
}
