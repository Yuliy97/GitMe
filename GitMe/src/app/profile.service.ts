import { Injectable } from '@angular/core';
import { FormGroup,  FormBuilder,  Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';
import {RequestOptions, Request, RequestMethod} from '@angular/http';

interface ProfileResponse {
  username: string;
  total_commits: number;
  avatar: string;
  html_url: string;
}
@Injectable()
export class ProfileService {
  constructor(private http: HttpClient) { }

  getProfile(username: string) {
    const uri = 'http://127.0.0.1:5000/users/' + username;
    return this.http.get<ProfileResponse>(uri)
            .map(res => {
              return res;
            });
  }

}
