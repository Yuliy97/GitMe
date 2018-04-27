import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Http, Headers } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import { catchError } from 'rxjs/operators';
import 'rxjs/add/observable/throw';


@Injectable()
export class AuthService {
  username: string;
  constructor(
    private http: HttpClient,
  ) {
  }

  authenticate_user(username: string, password: string) {
    this.username = username;
    const uri = 'http://127.0.0.1:5000/authorize';
    return this.http.put<string>(uri + '?username=' + username + '&password=' + password, {})
            .map(res => {
              return res;
            });
  }
  update_database(username: string, password: string) {
    this.username = username;
    const uri = 'http://127.0.0.1:5000/update';
    return this.http.post<string>(uri + '?username=' + username + '&password=' + password, {})
            .map(res => {
              return res;
            });
  }
  getUsername() {
    return this.username;
  }

}
