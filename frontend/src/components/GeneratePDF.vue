<template>
  <div>
    <input v-model="name" placeholder="Name" class="text-blue-600 flex space-x-4 border-2 border-rose-600 " />
    <input v-model="last_name" placeholder="Last Name" class="text-blue-600 flex space-x-4 border-2 border-rose-600 "  />
    <input v-model="email" placeholder="Email" class="text-blue-600 flex space-x-4 border-2 border-rose-600 "  />
    <!-- Other input fields -->
    <button @click="generatePDF" class="text-blue-600 flex space-x-4 border-2 border-rose-600 " >Generate PDF</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      name: '',
      email: '',
      last_name: '',
      // Other data fields
    };
  },
  methods: {
    generatePDF() {
      const formData = {
        name: this.name,
        email: this.email,
        last_name: this.last_name,
        // Other form data
      };

      axios.post('/backend/generate_pdf', formData, { responseType: 'blob' })
          .then(response => {
            // Create a URL for the blob response
            const url = window.URL.createObjectURL(new Blob([response.data]));

            // Create a temporary <a> element to trigger the download
            const link = document.createElement('a');
            link.href = url;
            link.setAttribute('download', 'generated.pdf');
            document.body.appendChild(link);
            link.click();
          })
          .catch(error => {
            // Handle error
            console.error(error);
          });
    }
  }
};
</script>
