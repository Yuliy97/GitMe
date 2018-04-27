import { Component, OnInit } from '@angular/core';
import { RepoService } from '../repo.service';
import { RepositoryResponse } from '../repo.service';
import { AuthService } from '../auth.service';
@Component({
  selector: 'app-repos',
  templateUrl: './repos.component.html',
  styleUrls: ['./repos.component.css']
})
export class ReposComponent implements OnInit {
  repos: RepositoryResponse[] = [];
  username: string;
  constructor(
    private _repoService: RepoService,
    private _authService: AuthService,
  ) { }

  ngOnInit() {
    this.getRepo();
  }
  getRepo() {
    this.username = this._authService.getUsername();
    this._repoService.getRepos(this.username).subscribe(
      data => {
        this.repos = data;
      }
    );
  }
  getMoreRepo(name: string) {
    name = this._authService.getUsername();
    this._repoService.getRepos(name).subscribe(
      data => {
        this.repos = data;
      }
    );
  }
}
