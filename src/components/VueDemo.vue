<template>
    <div class="hello">
        <p>Hello world</p>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: 'VueDemo',
        data() {
            return {
                info: null
            }
        },
        mounted() {
            axios
                .get('api/get_data')
                .then(response => {
                    this.info = response.data;
                    console.log(this.info);
                })
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    h3 {
        margin: 40px 0 0;
    }

    ul {
        list-style-type: none;
        padding: 0;
    }

    li {
        display: inline-block;
        margin: 0 10px;
    }

    a {
        color: #42b983;
    }

    img {
        width: 250px;
    }
</style>
