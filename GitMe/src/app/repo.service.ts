import { Injectable } from '@angular/core';
import { FormGroup,  FormBuilder,  Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';
import {RequestOptions, Request, RequestMethod} from '@angular/http';

export interface RepositoryResponse {
  repo_name: string;
  html_url: string;
  username: string;
  group_name: string;
}
@Injectable()
export class RepoService {

  constructor(private http: HttpClient) { }

  getRepos(username: string) {
    const uri = 'http://127.0.0.1:5000/users/' + username + '/repository';
    return this.http.get<RepositoryResponse[]>(uri)
            .map(res => {
              return res;
            });
  }

}
