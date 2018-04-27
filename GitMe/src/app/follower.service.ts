import { Injectable } from '@angular/core';
import { FormGroup,  FormBuilder,  Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';
import {RequestOptions, Request, RequestMethod} from '@angular/http';

@Injectable()
export class FollowerService {

  constructor(private http: HttpClient) { }

  getFollower(username: string) {
    const uri = 'http://127.0.0.1:5000/users/' + username + '/follower';
    return this.http.get<any[]>(uri)
            .map(res => {
              return res;
            });
  }

}
