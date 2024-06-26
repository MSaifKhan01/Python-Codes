// import { HttpClient } from '@angular/common/http';
// import { Component } from '@angular/core';

// @Component({
//   selector: 'app-crud',
//   templateUrl: './crud.component.html',
//   styleUrl: './crud.component.scss'
// })
// export class CrudComponent {

//   studentArray: any[] = [];
//   name: string = "";
//   address: string = "";
//   fee: number = 0;
//   currentStudentID = "";

//   constructor(private http: HttpClient) {
//     this.getAllStudents();
//   }

//   saveRecords() {
//     const bodyData = {
//       "name": this.name,
//       "address": this.address,
//       "fee": this.fee
//     };

//     this.http.post("http://127.0.0.1:8000/student", bodyData).subscribe((resultData: any) => {
//       console.log(resultData);
//       alert("Student Registered Successfully");
//       this.getAllStudents();
//     });
//   }

//   getAllStudents() {
//     this.http.get("http://127.0.0.1:8000/student").subscribe((resultData: any) => {
//       console.log(resultData);
//       this.studentArray = resultData;
//     });
//   }

//   setUpdate(student: any) {
//     this.name = student.name;
//     this.address = student.address;
//     this.fee = student.fee;
//     this.currentStudentID = student.id;
//   }

//   updateRecords() {
//     const bodyData = {
//       "name": this.name,
//       "address": this.address,
//       "fee": this.fee
//     };

//     this.http.put("http://127.0.0.1:8000/student/" + this.currentStudentID, bodyData).subscribe((resultData: any) => {
//       console.log(resultData);
//       alert("Student Updated Successfully");
//       this.name = '';
//       this.address = '';
//       this.fee = 0;
//       this.getAllStudents();
//     });
//   }

//   deleteRecord(student: any) {
//     this.http.delete("http://127.0.0.1:8000/student/" + student.id).subscribe((resultData: any) => {
//       console.log(resultData);
//       alert("Student Deleted Successfully");
//       this.getAllStudents();
//     });
//   }

// }


import { HttpClient, HttpParams } from '@angular/common/http';
import { Component } from '@angular/core';

@Component({
  selector: 'app-crud',
  templateUrl: './crud.component.html',
  styleUrls: ['./crud.component.scss']
})
export class CrudComponent {

  studentArray: any[] = [];
  name: string = "";
  address: string = "";
  fee: number = 0;
  currentStudentID = "";
  sortField: string = "";
  sortOrder: string = "asc";
  filterName: string = "";
  filterAddress: string = "";
  filterFee: string = "";

  constructor(private http: HttpClient) {
    this.getAllStudents();
  }

  saveRecords() {
    const bodyData = {
      "name": this.name,
      "address": this.address,
      "fee": this.fee
    };

    this.http.post("http://127.0.0.1:8000/student", bodyData).subscribe((resultData: any) => {
      console.log(resultData);
      alert("Student Registered Successfully");
      this.getAllStudents();
    });
  }

  getAllStudents() {
    let params = new HttpParams();
    if (this.sortField) {
      params = params.append('sort_by', this.sortField);
      params = params.append('sort_order', this.sortOrder);
    }
    if (this.filterName) {
      params = params.append('name', this.filterName);
    }
    if (this.filterAddress) {
      params = params.append('address', this.filterAddress);
    }
    if (this.filterFee) {
      params = params.append('fee', this.filterFee);
    }

    this.http.get("http://127.0.0.1:8000/student", { params }).subscribe((resultData: any) => {
      console.log(resultData);
      this.studentArray = resultData;
    });
  }

  setUpdate(student: any) {
    this.name = student.name;
    this.address = student.address;
    this.fee = student.fee;
    this.currentStudentID = student.id;
  }

  updateRecords() {
    const bodyData = {
      "name": this.name,
      "address": this.address,
      "fee": this.fee
    };

    this.http.put("http://127.0.0.1:8000/student/" + this.currentStudentID, bodyData).subscribe((resultData: any) => {
      console.log(resultData);
      alert("Student Updated Successfully");
      this.name = '';
      this.address = '';
      this.fee = 0;
      this.getAllStudents();
    });
  }

  deleteRecord(student: any) {
    this.http.delete("http://127.0.0.1:8000/student/" + student.id).subscribe((resultData: any) => {
      console.log(resultData);
      alert("Student Deleted Successfully");
      this.getAllStudents();
    });
  }

  sort(field: string) {
    if (this.sortField === field) {
      this.sortOrder = this.sortOrder === 'asc' ? 'desc' : 'asc';
    } else {
      this.sortField = field;
      this.sortOrder = 'asc';
    }
    this.getAllStudents();
  }

  // applyFilters() {
  //   this.getAllStudents();
  // }

  // clearFilters() {
  //   this.filterName = "";
  //   this.filterAddress = "";
  //   this.filterFee = "";
  //   this.getAllStudents();
  // }
}

