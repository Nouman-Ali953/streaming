<template>
    <div>
      <h1>Data Stream</h1>
      <ul>
        <li v-for="(chunk, index) in chunks" :key="index">{{ chunk }}</li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: "DataStream",
    data() {
      return {
        chunks: []  // Array to store streamed data
      };
    },
    mounted() {
      this.startStreaming();
    },
    methods: {
      startStreaming() {
        const eventSource = new EventSource("http://127.0.0.1:5000/api/stream");
        
        eventSource.onmessage = (event) => {
          this.chunks.push(event.data);  // Append each chunk to chunks array
        };
  
        eventSource.onerror = () => {
          eventSource.close();  // Close stream on error
        };
      }
    }
  };
  </script>
  
  <style scoped>
  h1 {
    color: #333;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    padding: 8px;
    background: #f4f4f4;
    margin: 4px 0;
    border-radius: 4px;
  }
  </style>
  