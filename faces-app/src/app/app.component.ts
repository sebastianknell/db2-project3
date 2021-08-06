import { Component } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { UploadService } from './upload.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'faces-app';
  file: File
  imgFile: string

  uploadForm = this.fb.group({
    file: new FormControl(null, [Validators.required]),
  });

  constructor(private uploadService: UploadService, private fb: FormBuilder) {}

  get uf() {
    return this.uploadForm.controls;
  }

  onImageChange(event) {
    let reader = new FileReader();

    if (event.target.files && event.target.files.length) {
      const [file] = event.target.files;
      reader.readAsDataURL(file);

      reader.onload = () => {
        this.uploadForm.patchValue({
          file: reader.result
        });

        // need to run CD since file load runs outside of zone
        // this.cd.markForCheck();
      };
    }
  }

  upload() {
    console.log(this.uploadForm.value)
    this.uploadService.uploadImage(this.uploadForm.value).subscribe(
      (res) => {
        console.log(res)
      },
      (err) => {
        console.log(err)
      })
  }
}
