import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-follower',
  templateUrl: './follower.component.html',
  styleUrls: ['./follower.component.css']
})
export class FollowerComponent implements OnInit {
  followers: any[] = [
    'James', 'Kirtan'
  ];

  constructor() { }

  ngOnInit() {
  }

}
