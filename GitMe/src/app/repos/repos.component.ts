import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-repos',
  templateUrl: './repos.component.html',
  styleUrls: ['./repos.component.css']
})
export class ReposComponent implements OnInit {
  repos: any[] = [{
    'url': 'www.github.com/r',
    'title': 'repo1'
  },
  {
    'url': 'www.github.com/yuli/gitme',
    'title': 'GitMe'
  }
  ];
  constructor() { }

  ngOnInit() {
  }

}
