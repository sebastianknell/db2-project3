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
  imgSrc: string;
  processingImage = true;

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
        this.imgSrc = reader.result as string
        this.uploadForm.patchValue({
          file: reader.result
        });
      };
    }
  }

  upload() {
    this.processingImage = true;
    this.uploadService.uploadImage(this.uploadForm.value).subscribe(
      (res) => {
        console.log(res);
        this.processingImage = false;
      },
      (err) => {
        this.processingImage = false;
        console.log(err);
      })
  }
}
