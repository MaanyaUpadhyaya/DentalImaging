import pydicom


def read_dicom_attributes(dcm_file):
    ds = pydicom.dcmread(dcm_file)
    print(ds)
    print("DICOM File:", dcm_file)
    print("Patient Name:", ds.PatientName)
    print("Patient ID:", ds.PatientID)
    print("Study Date:", ds.StudyDate)
    print("Modality:", ds.Modality)
    print("Image Width:", ds.Columns)
    print("Image Height:", ds.Rows)


dicom_file = "3DSlice1.dcm"
read_dicom_attributes(dicom_file)
