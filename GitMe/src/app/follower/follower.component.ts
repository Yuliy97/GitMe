import { Component, OnInit } from '@angular/core';
import { FollowerService } from '../follower.service';
import { FollowingService } from '../following.service';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-follower',
  templateUrl: './follower.component.html',
  styleUrls: ['./follower.component.css']
})
export class FollowerComponent implements OnInit {
  followers: any[] = [];
  followings: any[] = [];
  username: string;
  constructor(
    private _followerService: FollowerService,
    private _followingService: FollowingService,
    private _authService: AuthService
  ) { }

  ngOnInit() {
    this.getFollower();
    this.getFollowing();
  }

  getFollower() {
    this.username = this._authService.getUsername();
    this._followerService.getFollower(this.username).subscribe(
      data => {
        this.followers = data;
      }
    );
  }
  getFollowing() {
    this.username = this._authService.getUsername();
    this._followingService.getFollowing(this.username).subscribe(
      data => {
        this.followings = data;
      }
    );
  }

}
