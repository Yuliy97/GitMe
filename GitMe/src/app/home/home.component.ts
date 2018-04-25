import { Component, OnInit} from '@angular/core';
// import { CalendarComponent } from 'ng-fullcalendar';
// import { Options } from 'fullcalendar';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  issues: any[] = [
    {
      'title' : 'update',
      'state': 'open',
      'date': 'April 23rd, 2018',
      'description': 'updated gitme'
    },
    {
      'title' : 'comment',
      'state': 'open',
      'date': 'April 23rd, 2018',
      'description': 'uli: Kirtan wheres ur commits???? I need the API Boi!'
    },
    {
      'title' : 'issues',
      'state': 'open',
      'date': 'April 14rd, 2018',
      'description': 'need API update!'
    },
    {
      'title' : 'pullrequest',
      'state': 'open',
      'date': 'April 11rd, 2018',
      'description': 'james maded a pull request'
    },
  ];
  search: string;
  constructor() { }

  ngOnInit() {

  }
  searchFor() {

  }


}
