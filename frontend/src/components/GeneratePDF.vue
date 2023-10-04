<template>
  <div class="input-section" >
    <div class="input-section-header">Personal Information </div>
    <input v-model="name" placeholder="Name" class="input-field"  />
    <input v-model="last_name" placeholder="Last Name" class="input-field"  />
    <input v-model="email" placeholder="Email" class="input-field"  />

    <div class="input-section-header">Work Experience</div>
    <input v-model="company" placeholder="Company" class="input-field"  />
    <input v-model="position" placeholder="Position" class="input-field"  />
    <input v-model="duration" placeholder="Duration" class="input-field"  />
    <!-- Other input fields -->
    <button @click="generatePDF" class="input-button" >Generate PDF</button>
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
      company: '',
      position: '',
      duration: '',
      // Other data fields
    };
  },
  methods: {
    generatePDF() {
      const formData = {
        name: this.name,
        email: this.email,
        last_name: this.last_name,
        company: this.company,
        position: this.position,
        duration: this.duration
        // Other form data
      };

      axios.post('/backend/generate_pdf', JSON.stringify(formData), { responseType: 'blob' })
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
