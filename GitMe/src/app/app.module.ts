import { BrowserModule } from '@angular/platform-browser';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import { NgModule } from '@angular/core';
import { HomeComponent } from './home/home.component';
import { AppComponent } from './app.component';
import { DialogComponent } from './dialog/dialog.component';
import { WelcomeComponent } from './welcome/welcome.component';
import { RouterModule, Routes } from '@angular/router';
import { MatToolbarModule } from '@angular/material/toolbar';
import { HttpClientModule } from '@angular/common/http';
import { HttpModule } from '@angular/http';
import { MatDialogModule } from '@angular/material/dialog';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import {CdkTableModule} from '@angular/cdk/table';
import { FullCalendarModule } from 'ng-fullcalendar';
import { MyDatePickerModule } from 'mydatepicker';
import { ProfileService } from './profile.service';
import { FeedsService } from './feeds.service';
import {Observable} from 'rxjs/observable';
import {
  MatAutocompleteModule,
  MatButtonModule,
  MatButtonToggleModule,
  MatCardModule,
  MatCheckboxModule,
  MatChipsModule,
  MatDatepickerModule,
  MatDividerModule,
  MatExpansionModule,
  MatGridListModule,
  MatIconModule,
  MatInputModule,
  MatListModule,
  MatMenuModule,
  MatNativeDateModule,
  MatPaginatorModule,
  MatProgressBarModule,
  MatProgressSpinnerModule,
  MatRadioModule,
  MatRippleModule,
  MatSelectModule,
  MatSidenavModule,
  MatSliderModule,
  MatSlideToggleModule,
  MatSnackBarModule,
  MatSortModule,
  MatStepperModule,
  MatTableModule,
  MatTabsModule,
  MatTooltipModule,
  MatFormFieldModule
} from '@angular/material';
import * as $ from 'jquery';
import { EventsComponent } from './events/events.component';
import { FollowerComponent } from './follower/follower.component';
import { ReposComponent } from './repos/repos.component';
import { FollowerService } from './follower.service';
import { FollowingService } from './following.service';
import { RepoService } from './repo.service';
import { AuthService } from './auth.service';
import { AddAccountComponent } from './add-account/add-account.component';
import { NgxSpinnerModule } from 'ngx-spinner';
const routes: Routes = [
  {
    path: '',
    component: WelcomeComponent,
    children: []
  },
  {
    path: 'home',
    component: HomeComponent,
  },
  {
    path: 'event',
    component: EventsComponent,
  }
];
@NgModule({
  declarations: [
    AppComponent,
    WelcomeComponent,
    HomeComponent,
    DialogComponent,
    EventsComponent,
    FollowerComponent,
    ReposComponent,
    AddAccountComponent,
  ],
  imports: [
    NgxSpinnerModule,
    MatTabsModule,
    MatListModule,
    MyDatePickerModule,
    FullCalendarModule,
    MatExpansionModule,
    BrowserModule,
    MatButtonModule,
    MatToolbarModule,
    MatDialogModule,
    MatCardModule,
    FormsModule,
    HttpModule,
    MatSnackBarModule,
    HttpClientModule,
    HttpModule,
    MatFormFieldModule,
    BrowserAnimationsModule,
    MatSidenavModule,
    MatInputModule,
    RouterModule.forRoot(routes)
  ],
  exports: [
    HttpClientModule,
    MatFormFieldModule,
    CdkTableModule,
    MatAutocompleteModule,
    MatButtonModule,
    MatButtonToggleModule,
    MatCardModule,
    MatCheckboxModule,
    MatChipsModule,
    MatStepperModule,
    MatDatepickerModule,
    MatDialogModule,
    MatDividerModule,
    MatExpansionModule,
    MatGridListModule,
    MatIconModule,
    MatInputModule,
    MatListModule,
    MatMenuModule,
    MatNativeDateModule,
    MatPaginatorModule,
    MatProgressBarModule,
    MatProgressSpinnerModule,
    MatRadioModule,
    MatRippleModule,
    MatSelectModule,
    MatSidenavModule,
    MatSliderModule,
    MatSlideToggleModule,
    MatSnackBarModule,
    MatSortModule,
    MatTableModule,
    MatTabsModule,
    MatToolbarModule,
    MatTooltipModule,
  ],
  providers: [
    DialogComponent,
    FeedsService,
    ProfileService,
    FollowerService,
    FollowingService,
    RepoService,
    AuthService,
    ReposComponent
  ],
  bootstrap: [AppComponent],
  entryComponents: [
    DialogComponent, AddAccountComponent
  ]
})
export class AppModule { }
