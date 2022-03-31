<template>
  <div>
    <form
      action="/upload"
      method="post"
      enctype="multipart/form-data"
      @submit.prevent="onSubmit"
      @change="onChange"
    >
      <input type="file" @change="onFileChange" />
      <div>
        <img v-for="image in images" :key="image.index" :src="image.url" />
      </div>
      <button type="submit" @submit="handleSubmit">Upload</button>
    </form>
  </div>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      images: [],
    };
  },
  methods: {
    onFileChange(e) {
      const files = e.target.files || e.dataTransfer.files;
      if (!files.length) return;
      this.createImage(files[0]);
    },
    createImage(file) {
      const reader = new FileReader();
      const vm = this;
      reader.onload = (e) => {
        vm.images.push({
          url: e.target.result,
          index: vm.images.length,
        });
      };
      reader.readAsDataURL(file);
    },
    handleSubmit(e) {
      e.preventDefault();
      const formData = new FormData();
      this.images.forEach((image) => {
        formData.append("images[]", image.url);
      });
      axios
        .post("/upload", formData)
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
