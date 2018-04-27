import { Injectable } from '@angular/core';
import { FormGroup,  FormBuilder,  Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';
import {RequestOptions, Request, RequestMethod} from '@angular/http';

export interface FeedResponse {
  id: number;
  content: string;
  date: number;
  html_url: string;
  type: string;
  repo_url: string;
}

@Injectable()
export class FeedsService {

  constructor(private http: HttpClient) { }

  getFeeds(username: string) {
    const uri = 'http://127.0.0.1:5000/users/' + username + '/feed_entity';
    return this.http.get<FeedResponse[]>(uri)
            .map(res => {
              return res;
            });
  }

}
