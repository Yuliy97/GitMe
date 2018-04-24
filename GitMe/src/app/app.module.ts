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
const routes: Routes = [
  {
    path: '',
    component: WelcomeComponent,
    children: []
  },
  {
    path: 'home',
    component: HomeComponent,
  }
];
@NgModule({
  declarations: [
    AppComponent,
    WelcomeComponent,
    HomeComponent,
    DialogComponent
  ],
  imports: [
    MyDatePickerModule,
    FullCalendarModule,
    MatExpansionModule,
    BrowserModule,
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
  providers: [ DialogComponent ],
  bootstrap: [AppComponent],
  entryComponents: [
    DialogComponent,
  ]
})
export class AppModule { }
