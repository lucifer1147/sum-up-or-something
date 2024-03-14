<script>
	import { goto } from '$app/navigation';
	import { currActiveProfPage } from './store';
	import Profile from './profilepage.svelte';
	import Photo from './photopage.svelte';

	export let data;

	const back = () => {
		goto('/dashboard');
	};
</script>

<div class="bg-white h-full w-[75%] rounded-2xl pb-10">
	<div class="flex">
		<button class="h-20 w-20 rounded-xl p-4 inline-block" on:click={back}>
			<div class="h-full w-full rounded-3xl border-4 p-2 border-slate-900 fill-slate-900 flex">
				<svg
					xmlns="http://www.w3.org/2000/svg"
					viewBox="0 0 512 512"
					class="h-full relative right-0.5"
					><path
						d="M459.5 440.6c9.5 7.9 22.8 9.7 34.1 4.4s18.4-16.6 18.4-29V96c0-12.4-7.2-23.7-18.4-29s-24.5-3.6-34.1 4.4L288 214.3V256v41.7L459.5 440.6zM256 352V256 128 96c0-12.4-7.2-23.7-18.4-29s-24.5-3.6-34.1 4.4l-192 160C4.2 237.5 0 246.5 0 256s4.2 18.5 11.5 24.6l192 160c9.5 7.9 22.8 9.7 34.1 4.4s18.4-16.6 18.4-29V352z"
					/></svg
				>
			</div>
		</button>

		<div
			class="text-3xl text-center h-20 flex items-center ml-10 font-mono font-bold text-slate-900"
		>
			<h1>{$currActiveProfPage}:</h1>
		</div>
	</div>
	<hr class="border-black border-4" />

	<div class="h-full">
		{#if $currActiveProfPage === 'Profile'}
			<Profile {data} />
		{:else if $currActiveProfPage === 'Photo'}
			<Photo {data} />
		{/if}
	</div>
</div>

<svelte:window
	on:keydown={(e) => {
		if (e.code === 'Escape') {
			back();
		}
	}}
/>
