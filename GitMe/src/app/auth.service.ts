import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Http, Headers } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import { catchError } from 'rxjs/operators';
import 'rxjs/add/observable/throw';
@Injectable()
export class AuthService {
  private url = 'http://127.0.0.1:5000/update';
  constructor(
    private http: HttpClient,
  ) { }

}
