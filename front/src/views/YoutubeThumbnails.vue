<template>
    <div class="container mt-4 pt-2 pb-1">
        <div class="row">
            <div class="col">
                <h3 class="text-white d-flex d-lg-flex justify-content-center text-shadow">
                    {{ title }}
                </h3>
            </div>
        </div>
        <div class="row mb-4">
            <div class="col">
                <div class="row row-cols-1 row-cols-sm-1 row-cols-md-2 row-cols-lg-3 youtube">
                    <div class="col" v-for="(item, index) in items" :key="index">
                        <a :href="item.link">
                            <img class="rounded img-fluid shadow w-100 fit-cover img-thumbnail" :src="item.image" />
                        </a>
                        <div class="image-description rounded-bottom px-2">
                            <p>{{ item.description }}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            title: 'New Title',
            items: [
                {
                    link: '#',
                    image: 'new-image1.webp',
                    description: 'New description 1'
                },
                {
                    link: '#',
                    image: 'new-image2.webp',
                    description: 'New description 2'
                },
                {
                    link: '#',
                    image: 'new-image3.webp',
                    description: 'New description 3'
                }
            ]
        }
    }
}
</script>
