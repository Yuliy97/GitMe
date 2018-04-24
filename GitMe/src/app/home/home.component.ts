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
  // _events = [{title: 'Mission Support Capstone', start: '2018-04-23', end: '2018-04-24'}];
  // calendarOptions: Options;
  // event_name: string;
  // attendees: string;
  // event_description: string;
  // start_date: string;
  // end_date: string;
  // @ViewChild(CalendarComponent) ucCalendar: CalendarComponent;
  constructor() { }

  ngOnInit() {
    // this.calendarOptions = {
    //   editable: true,
    //   eventLimit: false,
    //   header: {
    //     left: 'prev,next today',
    //     center: 'title',
    //     right: 'month,agendaWeek,agendaDay,listMonth'
    //   },
    //   events: this._events,
    //     eventColor: '#378006',
    //     eventTextColor: 'white',
    //     eventClick: function(event) {
    //       console.log('HELLO');
    //       alert('Event ' + event.title);
    //     }
    // };
  }
  // on_add() {
  //   const event = {
  //     title: this.event_name,
  //     start: '2018-04-25',
  //     end: '2018-04-26'
  //   };
  //   this.ucCalendar.fullCalendar('renderEvent', event);
  // }

}
