const maxUploadSize = document.querySelector('meta[name="maxUploadSize"]').getAttribute('content');

const uploadsElement = document.querySelector('.uploads');
const previewTemplateElement = document.querySelector('#previewTemplate');

const previewTemplate = previewTemplateElement.innerHTML;
previewTemplateElement.parentNode.removeChild(previewTemplateElement);

const dropzone = new Dropzone(document.body, {
    url: '/upload',
    paramName: 'files',
    maxFilesize: maxUploadSize,
    parallelUploads: 2,
    thumbnailHeight: 50,
    thumbnailWidth: 50,
    uploadMultiple: false,
    maxFiles: 100,
    autoQueue: true,
    previewsContainer: '.uploads',
    previewTemplate: previewTemplate,
    clickable: '#upload',
    dictFileTooBig: 'File is too big! ({{filesize}}MB > {{maxFilesize}}MB)',
    dictResponseError: 'Something went wrong! ({{statusCode}})'
});

dropzone.on('addedfile', file => {
    uploadsElement.classList.remove('hidden');
});

dropzone.on('uploadprogress', (file, progress, byteSent) => {
    file.previewElement.querySelector('.file-progress .progress-inner').style.width = progress + '%';
});

dropzone.on('complete', file => {
    file.previewElement.querySelector('.upload-progress').classList.add('hidden');

    if (!file.xhr || !file.xhr.response) return;
    const data = JSON.parse(file.xhr.response);
    if (!data.files || !data.files.length) return;

    file.previewElement.querySelector('.upload-done').classList.remove('hidden');
    file.previewElement.querySelector('.link a').innerText = data.files[0].url;
    file.previewElement.querySelector('.link a').setAttribute('href', data.files[0].url);
});
