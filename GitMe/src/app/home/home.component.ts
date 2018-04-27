import { Component, OnInit} from '@angular/core';
// import { CalendarComponent } from 'ng-fullcalendar';
// import { Options } from 'fullcalendar';
import { ProfileService } from '../profile.service';
import { FeedsService } from '../feeds.service';
import { FeedResponse } from '../feeds.service';


interface ProfileResponse {
  username: string;
  total_commits: number;
  avatar: string;
  html_url: string;
}
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})

export class HomeComponent implements OnInit {
  issues: FeedResponse[] = [];
  search: string;
  username: string;
  totalCommit: number;
  avatar: string;
  html_url: string;
  constructor(
    private _profileService: ProfileService,
    private _feedService: FeedsService,
  ) { }
  ngOnInit() {
    this.getProfile();
    this.getFeeds();

  }
  searchFor() {

  }
  getProfile() {
    this._profileService.getProfile('jgormley6').subscribe(
      data => {
        this.totalCommit = data.total_commits;
        this.html_url = data.html_url;
        this.avatar = data.avatar;
        this.username = data.username;
      }
    );
  }
  getFeeds() {
    this._feedService.getFeeds('jgormley6').subscribe(
      data => {
        this.issues = data;
      }
    );
  }


}
