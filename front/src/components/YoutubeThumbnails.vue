<template>
    <div class="container mt-4 pt-2 pb-1" style="
          background: rgba(255, 241, 220, 0.18);
          margin-right: 0;
          margin-left: 0;
          width: 100%;
          display: block;
          max-width: none;
        ">
        <div class="row">
            <div class="col">
                <h3 class="text-white d-flex d-lg-flex justify-content-center text-shadow"
                    style="font-family: 'M PLUS 1', sans-serif">
                    動画
                </h3>
            </div>
        </div>
        <div class="row mb-4">
            <div class="col" v-if="!loading">
                <div class="row row-cols-1 row-cols-sm-1 row-cols-md-2 row-cols-lg-3 youtube">
                    <div class="col">
                        <a :href="`https://www.youtube.com/watch?v=${youtube[0].videoId}`" style="bornder: none">
                            <img class="rounded img-fluid shadow w-100 fit-cover img-thumbnail"
                                :src="youtube[0]?.thumbnail" />
                        </a>
                        <div class="image-description rounded-bottom px-2">
                            <p> {{ youtube[0]?.title }}</p>
                        </div>
                    </div>
                    <div class="col d-none d-sm-none d-md-block">
                        <a href="#">
                            <img class="rounded img-fluid shadow w-100 fit-cover img-thumbnail"
                                :src="youtube[1]?.thumbnail" />
                        </a>
                        <div class="image-description rounded-bottom px-2">
                            <p>{{ youtube[1]?.title }}
                            </p>
                        </div>
                    </div>
                    <div class="col d-none d-sm-none d-md-none d-lg-block">
                        <a href="#">
                            <img class="rounded img-fluid shadow w-100 fit-cover img-thumbnail"
                                :src="youtube[2]?.thumbnail" />
                        </a>
                        <div class="image-description rounded-bottom px-2">
                            <p>
                                {{ youtube[2]?.title }}
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapActions, mapState } from 'pinia'
import { useYoutubeStore } from '@/stores/media'
export default {
    name: 'YoutubeThumbnails',
    data() {
        return {
            loading: true
        }
    },
    methods: {
        ...mapActions(useYoutubeStore, ['fetchYoutubeInfo']),
    },
    computed: {
        ...mapState(useYoutubeStore, ['youtube']),
    },
    created() {
        this.fetchYoutubeInfo().then(() => {
            this.loading = false
        })
    },
}
</script>
