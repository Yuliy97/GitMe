import { Component, OnInit, ViewChild } from '@angular/core';
import { CalendarComponent } from 'ng-fullcalendar';
import { Options } from 'fullcalendar';
const _events = [{title: 'Class Presentation', start: '2018-04-19', end: '2018-04-19'}];
@Component({
  selector: 'app-events',
  templateUrl: './events.component.html',
  styleUrls: ['./events.component.css']
})
export class EventsComponent implements OnInit {
  calendarOptions: Options;
  event_name: string;
  attendees: string;
  event_description: string;
  start_date: string;
  end_date: string;
  @ViewChild(CalendarComponent) ucCalendar: CalendarComponent;

  constructor() { }

  ngOnInit() {
    this.calendarOptions = {
      editable: true,
      eventLimit: false,
      header: {
        left: 'prev,next today',
        center: 'title',
        right: 'month,agendaWeek,agendaDay,listMonth'
      },
      events: _events,
      eventColor: '#378006',
      eventTextColor: 'white',
      eventClick: function(event) {
        console.log('HELLO');
        alert('Event ' + event.title);
      }
    };
  }
// adding events frontend
  // start and end date should come from the modal that prompts user to fill out event details
  on_add() {
    const event = {
      title: this.event_name,
      start: '2018-04-25',
      end: '2018-04-26'
    };
    this.ucCalendar.fullCalendar('renderEvent', event);
  }
}
